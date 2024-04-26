import unittest
from docs.TestFiles.Persistreview import Review, ReviewRating, ReviewSchedule, ReviewComment

class TestReview(unittest.TestCase):
    def setUp(self):
        self.rating = ReviewRating(0,0,0,0)
        self.review = Review("SampleUser", "SampleTopic", "SampleContent", self.rating)

    def test_get_review(self):
        """
        Test the get_review class method of the Review class.
        """
        #create a sample rating
        SampleRating = ReviewRating(0,0,0,0)
        # Create a sample review and add it to the database
        review = Review("User1", "Topic1", "Content1", SampleRating)
        self.assertEqual(Review.get_review("User1", "Topic1", review.index), review, "Retrieved review should match the original.")

    def test_update_id(self):
        """
        Test the updateID class method of the Review class.
        """
        original_id = Review.reviewID
        Review.updateID()
        self.assertEqual(Review.reviewID, original_id + 1, "Review ID should be updated.")

    def test_remove_review(self):
        """
        Test the remove_review method of the Review class.
        """
        # Remove the review from the database
        Review.remove_review(self.review)
        self.assertIsNone(Review.get_review("SampleUser", "NewTopic", self.review.index), "Removed review should not be found in the database.")

    def test_get_author(self):
        self.assertEqual(self.review.get_author(), self.review.author, "Author should be same." )

    def test_equality(self):
        """
        Test the equality (__eq__) method of the Review class.
        """
        rating1 = ReviewRating(1,1,1,1)
        rating2 = ReviewRating(2,2,2,2)
        review1 = Review("User1", "Topic1", "Content1", rating1)
        review2 = Review("User1", "Topic1", "Content1", rating1)
        review3 = Review("User2", "Topic1", "Content1", rating2)
        review4 = Review("User1", "Topic2", "Content1", rating2)

        self.assertNotEqual(review1, review3, "Reviews with different authors should not be equal.")
        self.assertNotEqual(review2, review4, "Reviews with different topics should not be equal.")

if __name__ == "__main__":
    unittest.main()
