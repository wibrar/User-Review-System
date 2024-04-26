import unittest
from docs.TestFiles.Persistreview import Review, ReviewRating, ReviewSchedule, ReviewComment

class Test_ReviewComment(unittest.TestCase):
    def test_add_comment(self):
        # create a sample rating
        SampleRating = ReviewRating(0, 0, 0, 0)
        # Create a sample review and add it to the database
        SampleReview = Review("User1", "Topic1", "Content1", SampleRating)
        #Make Sample Comment for the review
        SampleComment = ReviewComment(SampleReview.get_author(), "SampleText")
        #append comment in Sample Review
        SampleReview.comments.append(SampleComment)

        self.assertEqual(SampleReview.comments[0], SampleComment, "Sample Comment should be saved.")  # add assertion here

if __name__ == '__main__':
    unittest.main()
