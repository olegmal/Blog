from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from blog.models import Post


class TestAPI(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.post = Post.objects.create(title="Post 1", fragment="Something about nothing 1", content="Content 1")
        # Post.objects.create(title="Post 2", fragment="Something about nothing 2", content="Content 2")

        self.user = get_user_model().objects.create(username="testuser", email="test_api@example.com")
        self.user.set_password("qwerty1234")
        self.user.save()

        self.superuser = get_user_model().objects.create(email="test_api_superuser@example.com", is_superuser=True)
        self.superuser.set_password("qwerty1234")
        self.superuser.save()

    def tearDown(self):
        Post.objects.all().delete()

    def test_list_posts(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.get(reverse("api:post_list"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f"{post.title}"
        self.assertEqual(expected_title, "Post 1")

    def test_fragment_content(self):
        post = Post.objects.get(id=1)
        expected_fragment = f"{post.fragment}"
        self.assertEqual(expected_fragment, "Something about nothing 1")

    def test_post_detail(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(
            reverse("api:post_detail", kwargs={"pk": self.post.pk})
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_create_post_with_invalid_data(self):
        data = {"title": "",
                "fragment": "Something invalid",
                "content": "Invalid content"}
        response = self.client.post(reverse("api:post_list"), data=data)
        self.assertEqual(response.status_code, 405)
        # self.assertEqual(response.data['title'][0], 'This field is required.')
