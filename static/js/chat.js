/// <reference path="jquery-3.6.1.js" />

// CONSTANTS
const LOAD_MORE_HTML = `<button class="btn btn-primary me-auto ms-auto">Load More</button>`;
const IS_SELLER = window.location.href.indexOf("user") != -1;
let showLoadMoreBtn = false;
let messages = [];

function getMessages(beforeId, afterId, cb) {
  let requestUrl = new URL(
    "/chat/messages/" + channelId,
    window.location.origin
  );

  if (beforeId) requestUrl.searchParams.set("before", beforeId);
  if (afterId) requestUrl.searchParams.set("after", afterId);

  $.getJSON(requestUrl.toString(), (data) => {
    showLoadMoreBtn = data.length == 50;
    cb(data);
  });
}

function drawChat() {
  const chatArea = document.getElementById("chat-area");
  chatArea.innerHTML = "";

  messages.map((message) => {
    const $loadMoreBtn = $(LOAD_MORE_HTML);
    $loadMoreBtn.click(() => {
      getMessages(messages[0].pk, null, (data) => {
        messages = [...data, ...messages];
        drawChat();
      });
    });

    if (showLoadMoreBtn) $(chatArea).append($loadMoreBtn);

    const newDiv = document.createElement("div");
    const newContent = document.createTextNode(message.fields.pesan);

    newDiv.appendChild(newContent);
    newDiv.classList.add("chat-item");
    if (
      (message.fields.pengirim == "pengirim" && IS_SELLER) ||
      (message.fields.pengirim == "user" && !IS_SELLER)
    ) {
      newDiv.classList.add("me");
    }

    chatArea.appendChild(newDiv);
  });
}

function submitChat(e) {
  e.preventDefault();

  let lastId = -1;
  if (messages.length > 0) {
    lastId = messages[messages.length - 1].pk;
  }

  $form = $("#chat-form");
  $.ajax({
    type: "POST",
    url: "/chat/messages/send",
    data: $form.serialize(), // serializes the form's elements.
    success: () => {
      getMessages(null, lastId, (data) => {
        messages.push(...data);
        drawChat();
        $form.trigger("reset");
      });
    },
  });
}

$(function () {
  getMessages(null, null, (data) => {
    messages = data;
    drawChat();
  });

  $("#chat-btn").click(submitChat);

  setInterval(() => {
    let lastId = -1;
    if (messages.length > 0) {
      lastId = messages[messages.length - 1].pk;
    }

    getMessages(null, lastId, (data) => {
      messages.push(...data);
      drawChat();
    });
  }, 5000);
});
