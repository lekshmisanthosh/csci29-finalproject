from django.db import models

# Create your models here.
class UserResponse(models.Model):
    """Model representing a book genre."""

    created_time = models.DateTimeField(auto_now=True)
    user_response = models.TextField(
        help_text="Enter any text you like. Please do not enter any PII information."
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.user_response
