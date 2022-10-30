from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Channel
from katalog.models import Toko


class ChatTestCase(TestCase):
    def setUp(self) -> None:
        self.test1 = User.objects.create_user(
            "test1", "test1@test.com", "password123", first_name="Test1"
        )
        self.test2 = User.objects.create_user(
            "test2", "test2@test.com", "password123", first_name="Test2"
        )
        self.test3 = User.objects.create_user(
            "test3", "test3@test.com", "password123", first_name="Test3"
        )
        self.test4 = User.objects.create_user(
            "test4", "test4@test.com", "password123", first_name="Test4"
        )

        self.toko1 = Toko.objects.create(
            nama="Contoh 1",
            kota="Depok",
            provinsi="Jawa Barat",
            lokasi="Jl. Contoh",
            deskripsi="Contoh",
            range_harga="mahal",
            buka=True,
            kondisi="ramai",
            pemilik=self.test1,
        )
        self.toko2 = Toko.objects.create(
            nama="Contoh 2",
            kota="Depok",
            provinsi="Jawa Barat",
            lokasi="Jl. Contoh",
            deskripsi="Contoh",
            range_harga="mahal",
            buka=True,
            kondisi="ramai",
            pemilik=self.test2,
        )

    def test_index(self):
        self.client.force_login(self.test3)
        r = self.client.get("/chat/")
        self.assertEqual(r.status_code, 200)

    def test_sidebar(self):
        self.client.force_login(self.test3)
        r = self.client.get("/chat/toko/1")
        self.assertContains(r, "Tidak ada pesan")

        channel = Channel.objects.get(user=self.test3, toko=self.toko1)
        self.client.post(
            "/chat/messages/send", {"pesan": "Contoh pesan user", "cid": channel.pk}
        )

        r = self.client.get("/chat/")
        self.assertContains(r, "Contoh pesan user")

    def test_sidebar_order(self):
        self.client.force_login(self.test4)
        self.client.get("/chat/toko/1")
        r = self.client.get("/chat/toko/2")

        channel_toko1 = Channel.objects.get(user=self.test4, toko=self.toko1)
        channel_toko2 = Channel.objects.get(user=self.test4, toko=self.toko2)

        html_content: str = r.content.decode()
        self.assertLess(html_content.index("Contoh 1"), html_content.index("Contoh 2"))

        self.client.post(
            "/chat/messages/send",
            {"pesan": "Contoh pesan user", "cid": channel_toko2.pk},
        )

        self.client.post(
            "/chat/messages/send",
            {"pesan": "Contoh pesan user", "cid": channel_toko1.pk},
        )

        self.assertGreater(
            html_content.index("Contoh 1"), html_content.index("Contoh 2")
        )

    def test_never_chat_before(self):
        self.client.force_login(self.test3)
        r = self.client.get("/chat/toko/1")
        self.assertContains(r, "Contoh 1")

        # Check existence, should never return exception
        Channel.objects.get(user=self.test3, toko=self.toko1)

        self.client.force_login(self.test1)
        r = self.client.get("/chat/user/4")
        self.assertContains(r, "Test4")

        # Check existence, should never return exception
        Channel.objects.get(user=self.test4, toko=self.toko1)

    def test_self_message(self):
        self.client.force_login(self.test1)
        r = self.client.get("/chat/user/1")
        self.assertContains(r, "Cannot message with yourself")

        r = self.client.get("/chat/toko/1")
        self.assertContains(r, "Cannot message with yourself")

    def test_nonexistent(self):
        self.client.force_login(self.test1)
        r = self.client.get("/chat/user/9")
        self.assertContains(r, "does not exist")

        r = self.client.get("/chat/toko/9")
        self.assertContains(r, "does not exist")

    def test_user_as_toko(self):
        self.client.force_login(self.test3)
        r = self.client.get("/chat/user/1")
        self.assertContains(r, "do not have a store")

    def test_messaging(self):
        self.client.force_login(self.test3)
        self.client.get("/chat/toko/1")

        channel = Channel.objects.get(user=self.test3, toko=self.toko1)
        r = self.client.post(
            "/chat/messages/send", {"pesan": "Contoh pesan user", "cid": channel.pk}
        )
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, b"OK")

        self.client.force_login(self.test1)
        r = self.client.post(
            "/chat/messages/send", {"pesan": "Contoh pesan toko", "cid": channel.pk}
        )
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, b"OK")

        r = self.client.get(f"/chat/messages/{channel.pk}")
        self.assertJSONEqual(
            r.content.decode(),
            [
                {
                    "model": "chat.pesan",
                    "pk": 1,
                    "fields": {
                        "pesan": "Contoh pesan user",
                        "pengirim": "user",
                        "channel": 1,
                    },
                },
                {
                    "model": "chat.pesan",
                    "pk": 2,
                    "fields": {
                        "pesan": "Contoh pesan toko",
                        "pengirim": "pengirim",
                        "channel": 1,
                    },
                },
            ],
        )
