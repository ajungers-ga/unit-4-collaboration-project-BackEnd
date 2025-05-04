from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from reading_materials.models import ReadingMaterial
from reviews.models import Review
from news.models import News

class Command(BaseCommand):
    help = 'Populates the database with initial reading material and review data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')
        
        # Delete existing data (optional - comment out if not needed)
        self.stdout.write('Clearing existing data...')
        Review.objects.all().delete()
        ReadingMaterial.objects.all().delete()
        
        # Create books - reduced to 3 sample items
        self.stdout.write('Creating reading materials...')
        
        books_data = [
            {
                "title": "The Midnight Library",
                "authorName": "Matt Haig",
                "coverImage": "https://via.placeholder.com/300x450?text=The+Midnight+Library",
                "rating": 9.3,
                "publicationDate": "2020-08-13",
                "categories": ["Fiction", "Fantasy", "Philosophy"],
                "description": "It's the story of Nora Seed, who finds herself in a vast library between life and death. Every book represents a different version of her life she could have lived. As Nora explores the infinite possibilities of her choices, she must search within herself to decide what makes life worth living.",
                "type": "Book",
                "readingStatus": "unread"
            },
            {
                "title": "The Silent Patient",
                "authorName": "Alex Michaelides",
                "coverImage": "https://via.placeholder.com/300x450?text=The+Silent+Patient",
                "rating": 8.1,
                "publicationDate": "2019-02-05",
                "categories": ["Crime", "Thriller", "Mystery"],
                "description": "Alicia Berenson's life is seemingly perfect. A famous painter married to an in-demand fashion photographer, she lives in a grand house with big windows overlooking a park in one of London's most desirable areas. One evening her husband Gabriel returns home late from a fashion shoot, and Alicia shoots him five times in the face, and then never speaks another word.",
                "type": "Book",
                "readingStatus": "unread"
            },
            {
                "title": "Educated",
                "authorName": "Tara Westover",
                "coverImage": "https://via.placeholder.com/300x450?text=Educated",
                "rating": 8.6,
                "publicationDate": "2018-02-20",
                "categories": ["Memoir", "Biography", "Education"],
                "description": "Born to survivalists in the mountains of Idaho, Tara Westover was seventeen the first time she set foot in a classroom. Her family was so isolated from mainstream society that there was no one to ensure the children received an education, and no one to intervene when one of Tara's older brothers became violent.",
                "type": "Book",
                "readingStatus": "unread"
            },
            {
                "title": "Where the Crawdads Sing",
                "authorName": "Delia Owens",
                "coverImage": "https://via.placeholder.com/300x450?text=Where+the+Crawdads+Sing",
                "rating": 8.0,
                "publicationDate": "2018-08-14",
                "categories": ["Fiction", "Mystery", "Literary"],
                "description": "For years, rumors of the 'Marsh Girl' have haunted Barkley Cove, a quiet town on the North Carolina coast. So in late 1969, when handsome Chase Andrews is found dead, the locals immediately suspect Kya Clark, the so-called Marsh Girl. But Kya is not what they say.",
                "type": "Book",
                "readingStatus": "unread"
            },
            {
                "title": "The Humans",
                "authorName": "Matt Haig",
                "coverImage": "https://via.placeholder.com/300x450?text=The+Humans",
                "rating": 8.3,
                "publicationDate": "2013-05-09",
                "categories": ["Fiction", "Science Fiction", "Philosophy"],
                "description": "When an extraterrestrial visitor arrives on Earth, his first impressions of the human species are less than positive. But as time goes on, he starts to realize there may be more to this weird species than he had thought.",
                "type": "Book",
                "readingStatus": "unread"
            },
            {
                "title": "Project Hail Mary",
                "authorName": "Andy Weir",
                "coverImage": "https://via.placeholder.com/300x450?text=Project+Hail+Mary",
                "rating": 8.4,
                "publicationDate": "2021-05-04",
                "categories": ["Sci-Fi", "Adventure", "Space"],
                "description": "Ryland Grace is the sole survivor on a desperate, last-chance mission—and if he fails, humanity and the Earth itself will perish. Except that right now, he doesn't know that. He can't even remember his own name, let alone the nature of his assignment or how to complete it.",
                "type": "Book",
                "readingStatus": "unread"
            },
            {
                "title": "The Night Wanderer",
                "authorName": "Alex Michaelides",
                "coverImage": "https://via.placeholder.com/300x450?text=The+Night+Wanderer",
                "rating": 8.2,
                "publicationDate": "2023-09-12",
                "categories": ["Mystery", "Thriller", "Suspense"],
                "description": "A gripping mystery about a series of unexplained disappearances in a small coastal town, where locals begin to suspect a mysterious figure who only appears at night.",
                "type": "Book",
                "readingStatus": "unread"
            },
            {
                "title": "Chronicles of the Forgotten: The Fourth Seal",
                "authorName": "Nathan Cole",
                "coverImage": "https://via.placeholder.com/300x450?text=Chronicles+of+the+Forgotten",
                "rating": 8.7,
                "publicationDate": "2022-10-21",
                "categories": ["Fantasy", "Adventure", "Mythology"],
                "description": "An epic tale of heroes rising in a world torn by ancient wars, mythical beasts, and dark omens. The Fourth Seal has been broken, and the fate of the realms lies in uncertain hands.",
                "type": "Book",
                "readingStatus": "unread"
            }
        ]


        # Create book objects and store for reference in reviews
        book_objects = []
        
        for book_data in books_data:
            # Parse the date string to a Python date object
            if 'publicationDate' in book_data and book_data['publicationDate']:
                book_data['publicationDate'] = parse_date(book_data['publicationDate'])
            
            # Create the book
            book = ReadingMaterial.objects.create(**book_data)
            book_objects.append(book)
            self.stdout.write(f"Created reading material: {book.title}")

        # Reviews data mapping - reduced to 3 samples
        reviews_data = [
            {
                "bookIndex": 0,
                "reviewer_name": "Alice",
                "comment": "An incredibly moving and introspective book. I cried more than once reading Nora’s journey. A must-read for anyone who’s felt lost.",
                "rating": 5
            },
            {
                "bookIndex": 0,
                "reviewer_name": "Ben",
                "comment": "The concept is brilliant and well-executed. Matt Haig really knows how to write about mental health in a hopeful way.",
                "rating": 5
            },
            {
                "bookIndex": 1,
                "reviewer_name": "Chloe",
                "comment": "Kept me guessing until the end. I loved the psychological twists and how everything came together.",
                "rating": 4
            },
            {
                "bookIndex": 1,
                "reviewer_name": "David",
                "comment": "A little slow at first, but the payoff was worth it. Great for fans of dark thrillers.",
                "rating": 4
            },
            {
                "bookIndex": 2,
                "reviewer_name": "Ella",
                "comment": "This memoir blew me away. So raw and honest. Tara Westover’s story is unforgettable.",
                "rating": 5
            },
            {
                "bookIndex": 2,
                "reviewer_name": "Frank",
                "comment": "It’s both horrifying and inspiring. You won’t believe it’s a true story at times.",
                "rating": 4
            },
            {
                "bookIndex": 3,
                "reviewer_name": "Grace",
                "comment": "A slow burn but beautifully written. The marsh setting was so atmospheric.",
                "rating": 4
            },
            {
                "bookIndex": 3,
                "reviewer_name": "Henry",
                "comment": "I didn’t expect to enjoy this so much. The characters were vivid and well-developed.",
                "rating": 4
            },
            {
                "bookIndex": 4,
                "reviewer_name": "Isla",
                "comment": "Funny, philosophical, and weird in all the best ways. This book made me feel a little more human.",
                "rating": 4
            },
            {
                "bookIndex": 4,
                "reviewer_name": "Jack",
                "comment": "It’s a satire, a sci-fi, and a heartwarming story all at once. Really enjoyed it.",
                "rating": 4
            },
            {
                "bookIndex": 5,
                "reviewer_name": "Kate",
                "comment": "Just as fun as The Martian, maybe even better. Ryland Grace is a great protagonist.",
                "rating": 5
            },
            {
                "bookIndex": 5,
                "reviewer_name": "Liam",
                "comment": "A thrilling and surprisingly emotional ride through space. The science is deep but approachable.",
                "rating": 5
            },
            {
                "bookIndex": 6,
                "reviewer_name": "Maya",
                "comment": "Creepy and suspenseful with a clever twist. You’ll keep turning pages.",
                "rating": 4
            },
            {
                "bookIndex": 6,
                "reviewer_name": "Noah",
                "comment": "Well-paced and full of mystery. One of my favorite reads this year.",
                "rating": 4
            },
            {
                "bookIndex": 7,
                "reviewer_name": "Olivia",
                "comment": "Epic fantasy done right. The world-building is rich, and the characters are compelling.",
                "rating": 5
            },
            {
                "bookIndex": 7,
                "reviewer_name": "Paul",
                "comment": "Felt like reading a myth from another world. Gripping from start to finish.",
                "rating": 5
            }
        ]


        # Create reviews
        self.stdout.write('Creating reviews...')
        for review_data in reviews_data:
            book_index = review_data.pop('bookIndex')
            book = book_objects[book_index]
            
            # Create review with proper field names
            review = Review(
                reading_material=book,
                reviewer_name=review_data['reviewer_name'],
                comment=review_data['comment'],
                rating=review_data['rating']
            )
            
            review.save()
            self.stdout.write(f"Created review by {review.reviewer_name} for {book.title}")
        
        # Create news
        self.stdout.write('Clearing existing news items...')
        News.objects.all().delete()
        # News data
        self.stdout.write('Creating news items...')
        news_data = [
            {
                "title": "\"The Night Wanderer,\" the popular mystery novel, has been renewed for a sequel, much to the delight of its dedicated fanbase.",
                "content": "Publisher HarperCollins has announced that Alex Michaelides will be writing a sequel to his popular mystery novel \"The Night Wanderer\". The announcement comes after the book spent 15 weeks on the New York Times bestseller list. The sequel, tentatively titled \"The Dawn Seeker\", is expected to be released in late 2026.",
                "date": "2025-04-28",
                "image": "/images/newscard2.png",
                "author": "Literary Times"
            },
            {
                "title": "The highly anticipated fourth book in the \"Chronicles of the Forgotten\" series is set to premiere on September 4, 2025, promising more thrilling storylines and complex characters that readers have come to love.",
                "content": "Fans of Delia Owens' epic fantasy series have been eagerly awaiting the fourth installment, which was delayed by six months due to the author's extensive research trips. The publisher has revealed that this will be the longest book in the series yet, clocking in at over 400 pages. Early reviews from critics who received advance copies have been overwhelmingly positive.",
                "date": "2025-04-25",
                "image": "/images/newscard.png",
                "author": "Fantasy Book Review"
            },
            {
                "title": "Notable authors, including the acclaimed Gary Oldman and Cillian Murphy, will continue to bring depth and intrigue to the literary world with their upcoming releases.",
                "content": "In a surprising career pivot, award-winning actors Gary Oldman and Cillian Murphy have both announced debut novels to be published next year. Oldman's historical fiction \"The Unseen Hand\" and Murphy's psychological thriller \"Quiet Minds\" have already generated significant buzz in publishing circles, with film rights being discussed before the books have even hit shelves.",
                "date": "2025-04-20",
                "image": "/images/newscard1.png",
                "author": "Entertainment Weekly"
            },
            {
                "title": "Annual Book Festival to feature virtual reality reading rooms for the first time",
                "content": "This year's International Book Festival will introduce cutting-edge virtual reality reading rooms, allowing attendees to immerse themselves in settings from popular books. Visitors can experience everything from the Hogwarts Great Hall to the dystopian landscape of The Hunger Games, bringing literature to life in unprecedented ways.",
                "date": "2025-04-15",
                "image": "/images/newscard2.png",
                "author": "Tech & Literature"
            },
            {
                "title": "Study shows dramatic increase in audiobook consumption among young adults",
                "content": "A recent study by the National Reading Foundation has found that audiobook consumption among 18-25 year olds has increased by 45% over the past two years. This shift is attributed to the rise of multitasking culture and improvements in audiobook production quality, with full cast recordings and ambient sound effects becoming increasingly common.",
                "date": "2025-04-10",
                "image": "/images/newscard4.png",
                "author": "Publishing Insights"
            },
            {
                "title": "Local libraries embracing AI book recommendation systems",
                "content": "Public libraries across the country are adopting AI-powered recommendation systems to help readers discover new books. These systems analyze reading history and preferences to suggest titles readers might enjoy, with early data showing a 30% increase in circulation for libraries that have implemented the technology.",
                "date": "2025-04-05",
                "image": "/images/newscard5.png",
                "author": "Library Journal"
            }
        ]

        # Create news items
        for news_item in news_data:
            # Parse the date string to a Python date object
            if 'date' in news_item and news_item['date']:
                news_item['date'] = parse_date(news_item['date'])
            
            # Create the news item
            news = News.objects.create(**news_item)
            self.stdout.write(f"Created news item: {news.title[:50]}...")

        self.stdout.write(self.style.SUCCESS('News items created successfully!'))

        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))