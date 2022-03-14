from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django.utils.html import strip_tags
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from datetime import datetime
from django.contrib import  messages


class Category(models.Model):
    """
    The Category Model used for representing post categories.
    """
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True, default='no-slug')
    order = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        ordering = ['-order']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    The Tag Model used for representing post tags.
    """
    name = models.CharField(max_length=100, unique=True)
    slug =models.SlugField(max_length=100, blank=True, default='no-slug')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        

class Post(models.Model):
        """
        The Post Model used for representing blog post records and 
        which is related to User, Category, Tags models.
        """
        STATUS_CHOICES = (
                ('d', 'draft'),
                ('p', 'post'),
        )
        COMMENT_STATUS = (
                ('o', 'open'),
                ('c', 'close'),
        )
        title = models.CharField(max_length=200)
        slug = models.SlugField(unique=True, editable=False, max_length=150)
        excerpt = models.TextField(blank=True)
        content = RichTextField()
        created_date = models.DateTimeField(auto_now_add=True)
        modified_date = models.DateTimeField(auto_now=True)
        comment_count = models.PositiveIntegerField(default=0)
        view_count = models.PositiveIntegerField(default=0)
        category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
        tag = models.ManyToManyField(Tag, blank=True)
        author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
        comment_status = models.CharField(default='o', max_length=1, choices=COMMENT_STATUS)
        status = models.CharField(default='p', max_length=1, choices=STATUS_CHOICES)

        
        def image_rename(self, imagename):
            '''
            This method used for rename the uploaded image file.
            '''
            image_extension = imagename.split('.')[-1]
            user_name = self.author.username
            date_time_now = datetime.now().strftime("%Y-%m-%d-%H-%s")
            imagename = '{}-{}.{}'.format(user_name, date_time_now, image_extension)
            return imagename

        image = models.ImageField(null=True, blank=True, upload_to=image_rename)

        def get_unique_slug(self):
            '''
            This method used for generates and returns unique slugs.
            '''
            slug = self.title
            unique_slug = slugify(self.title)
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(slug, counter)
                counter += 1
            return unique_slug
        
        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = self.get_unique_slug()
            if self.image:
                self._resize_image()          
            return super(Post, self).save(*args, **kwargs)
        
        def _resize_image(self, *args, **kwargs):
            '''
            This method resize and returns of the self.image.
            '''
            super().save(*args, **kwargs)
            img = Image.open(self.image.path)
            if img.height > 1080 or img.width > 1080:
                output_image_size = (1080, 1080)
                img.thumbnail(output_image_size)
                return img.save(self.image.path)
                
        
        def increase_view_count(self):
            '''
            This method increses of the view count value for the post.
            '''
            self.view_count += 1
            self.save(update_fields=["view_count"])
            return
        
        def get_comments(self, *args, **kwargs):
            queryset = Comment.objects.filter(post=self.id)
            if queryset.exists():
                return queryset
            return []
            
        
        def __str__(self):
            return self.title
        
        class Meta:
            ordering = ['-created_date']


class Comment(models.Model):
    """
    The Comment Model used for representing post comments and 
    which is related to the Post model.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    content = models.TextField(help_text="Enter comment about post here.")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_date']
