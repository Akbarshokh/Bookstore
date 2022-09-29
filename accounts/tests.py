from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpPageView


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
            username="akbar", email="akbar@email.com", password="testpass123"
        )
        self.assertEqual(user.username, "akbar")
        self.assertEqual(user.email, "akbar@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    """new superuser creation test
    Parameters
    ----------
    TestCase : unit
        this test case confirms that a new superuser can be created
    """

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


class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi this an error page!)")

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken') 

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)
