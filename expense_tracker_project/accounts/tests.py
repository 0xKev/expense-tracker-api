from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model


class CustomUsersTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            email="foo@gmail.com",
            username="foo_user",
            password="foo_pass"
        )
        self.assertEqual(user.email, "foo@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


class ExpenseTest(TestCase):
    pass