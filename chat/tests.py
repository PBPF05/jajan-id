from django.test import TestCase
from django.contrib.auth.models import User
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

        Toko.objects.create(
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
        Toko.objects.create(
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

    def test_never_chat_before(self):
        self.client.force_login(self.test3)
        r = self.client.get("/chat/toko/1")
        self.assertContains(r, "Contoh 1")

        self.client.force_login(self.test1)
        r = self.client.get("/chat/user/4")
        self.assertContains(r, "Test4")

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
