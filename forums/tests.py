from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Forum, Thread, Post
from django.urls import reverse, resolve


class ForumTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='forumuser',
            email='forumuser@email.com',
            password='testpass123',
        )
        self.forum = Forum.objects.create(
            title='Testforum',
            description='A test forum'
        )
        self.thread = Thread.objects.create(
            title='Testtitle',
            forum_id=self.forum.id,
            user=self.user
        )
        self.post = Post.objects.create(
            text='This is the text in the first post',
            thread_id=self.thread.id,
            user=self.user
        )

    def test_forum_listing(self):
        self.assertEqual(f'{self.forum.title}', 'Testforum')
        self.assertEqual(f'{self.forum.description}', 'A test forum')

    def test_thread_listing(self):
        self.assertEqual(f'{self.thread.title}', 'Testtitle')
        self.assertEqual(f'{self.thread.user}', 'forumuser')
        self.assertEqual(f'{self.thread.forum.title}', 'Testforum')

    def test_post_listing(self):
        self.assertEqual(f'{self.post.text}', 'This is the text in the first post')
        self.assertEqual(f'{self.user}', 'forumuser')
        self.assertEqual(f'{self.post.thread.title}', 'Testtitle')


class ForumListPageTests(TestCase):

    def setUp(self):
        url = reverse('forum_list')
        print(url)
        self.response = self.client.get(url)

    def test_forum_list_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'forums/forum_list.html')
        self.assertContains(self.response, 'New forum')
        self.assertNotContains(self.response, 'This should not be here')


class ForumDetailPageTests(TestCase):

    def setUp(self):
        url = reverse('forum_detail', args=('1',))
        #print(url)
        self.response = self.client.get(url)

    def test_forum_detail_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'forums/forum_detail.html')
        self.assertContains(self.response, 'New thread')
        self.assertNotContains(self.response, 'This should not be here')
