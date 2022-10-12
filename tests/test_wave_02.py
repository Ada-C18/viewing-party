import pytest
from viewing_party.party import *
from tests.test_constants import *

# @pytest.mark.skip()


def test_calculates_watched_average_rating():
    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(3.58333)
    assert janes_data == clean_wave_2_data()


# @pytest.mark.skip()
def test_empty_watched_average_rating_is_zero():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)


# @pytest.mark.skip()
def test_most_watched_genre():
    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Fantasy"
    assert janes_data == clean_wave_2_data()


# @pytest.mark.skip()
def test_genre_is_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == None

# @pytest.mark.skip()
def test_Jaime_most_watched_genre():
    # Arrange
    janes_data = {   'watched': [   {   'genre': 'Horror',
                       'rating': 4.8,
                       'title': 'The Lord of the Functions: The Fellowship of '
                                'the Function'},
                   {   'genre': 'Drama',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Two '
                                'Parameters'},
                   {   'genre': 'Action',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Return of the '
                                'Value'},
                   {   'genre': 'Action',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Two Titles'
                                'Value'},
                   {   'genre': 'Action',
                       'rating': 2.2,
                       'title': 'The JavaScript and the React'},
                   {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
                   {   'genre': 'Intrigue',
                       'rating': 4.5,
                       'title': 'Instructor Student TA Manager'},
                   {   'genre': 'Action',
                       'rating': 4.0,
                       'title': "The Programmer's Daughter"}]}

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == 'Action'