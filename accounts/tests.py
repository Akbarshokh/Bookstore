from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    """new user creation test
    Parameters
    ----------
    TestCase : unit
        this test case confirms that a new user can be created
    """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="akbar", 
            email="akbar@email.com", 
            password="testpass123"
        )
        self.assertEqual(user.username, "akbar")
        self.assertEqual(user.email, "akbar@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="root",
            email="root@email.com",
            password="testpass123",
        )
        self.assertEqual(admin_user.username, "root")
        self.assertEqual(admin_user.email, "root@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
