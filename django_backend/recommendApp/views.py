from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Book  # Import your Book model here
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd

@csrf_exempt
def bookApi(request, id=0):
    if request.method=='GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    elif request.method=='POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        book_data = JSONParser().parse(request)
        book = Book.objects.get(bookid=book_data['bookid'])
        book_serializer = BookSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method=='DELETE':
        book = Book.objects.get(bookid=id)
        book.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def bookrecommendApi(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_history_books = data.get('user_history_books', [])
        user_study_area = data.get('user_study_area', '')

        csv_file_path = "./datasetmy.csv" # file path
        data = pd.read_csv(csv_file_path)

        # Create a Surprise Dataset
        reader = Reader(rating_scale=(1, 5))
        surprise_data = Dataset.load_from_df(data[['Field_of_Study', 'Book_Title', 'Rating']], reader)

        # Split the data into train and test sets
        trainset, testset = train_test_split(surprise_data, test_size=0.2, random_state=42)

        # Train an SVD model
        model = SVD(n_factors=50, random_state=42)
        model.fit(trainset)

        user_id = len(data['Book_Title'].unique())
        user_history_ratings = [model.predict(uid=user_id, iid=book).est for book in user_history_books]

        history_fields_of_study = set(data[data['Book_Title'].isin(user_history_books)]['Field_of_Study'].unique())

        recommendations = []
        if history_fields_of_study:
            for book in data['Book_Title'].unique():
                book_field_of_study = data[data['Book_Title'] == book]['Field_of_Study'].values[0]
                if (
                    book not in user_history_books
                    and book_field_of_study in history_fields_of_study
                ):
                    predicted_rating = model.predict(uid=user_id, iid=book).est
                    recommendations.append((book, predicted_rating))

        recommendations.sort(key=lambda x: x[1], reverse=True) # highest first
        book_titles_array = [book for book, _ in recommendations]

        return JsonResponse(book_titles_array, safe=False)

    return JsonResponse("Invalid Request Method", safe=False)