from datetime import date

from flask import Flask, abort, flash, redirect, render_template, request, url_for

from planning import db, Movie, Genre, Review


def add_starting_movies():
    action = Genre(
        genre_name="Action",
        description="Fast-paced movies with exciting scenes"
    )

    adventure = Genre(
        genre_name="Adventure",
        description="Movies involving journeys and exploration"
    )

    drama = Genre(
        genre_name="Drama",
        description="Movies focused on emotions and character development"
    )

    scifi = Genre(
        genre_name="Sci-Fi",
        description="Science fiction and futuristic stories"
    )

    thriller = Genre(
        genre_name="Thriller",
        description="Suspenseful and exciting movies"
    )

    db.session.add_all([action, adventure, drama, scifi, thriller])

    movie_data = [
        ("Avatar", date(2009, 12, 18), 2923706026, "A disabled Marine travels to Pandora and becomes caught between humanity and the Na'vi people.", "avatar imdb.jpg", [action, adventure, scifi]),
        ("Avatar: The Way of Water", date(2022, 12, 16), 2320250281, "Jake Sully and Neytiri fight to protect their family from a returning human threat on Pandora.", "avatar way of water imdb.jpg", [action, adventure, scifi]),
        ("Avengers Endgame", date(2019, 4, 26), 2799439100, "The remaining Avengers attempt one final mission to reverse Thanos' actions and restore the universe.", "Avengers Endgame imdb.jpg", [action, adventure, scifi]),
        ("Avengers Infinity War", date(2018, 4, 27), 2052415039, "The Avengers unite to stop Thanos from collecting all six Infinity Stones.", "Avengers Infinity War imdb.jpg", [action, adventure, scifi]),
        ("Titanic", date(1997, 12, 19), 2264750694, "A young couple from different social classes fall in love aboard the ill-fated RMS Titanic.", "titanic imdb.jpg", [drama]),
        ("Inception", date(2010, 7, 16), 839030630, "A skilled thief enters people's dreams to steal secrets but is offered a chance at redemption.", "Inception imdb.jpg", [action, thriller, scifi]),
        ("Interstellar", date(2014, 11, 7), 731001720, "A team of astronauts travel through a wormhole in search of humanity's new home.", "Interstellar.jpg", [adventure, drama, scifi]),
        ("The Dark Knight", date(2008, 7, 18), 1006234167, "Batman faces the Joker, a criminal mastermind who pushes Gotham City into chaos.", "dark knight.jpg", [action, thriller]),
        ("The Batman", date(2022, 3, 4), 772245583, "Batman investigates a series of murders committed by the mysterious Riddler.", "batman.jpg", [action, thriller]),
        ("Joker", date(2019, 10, 4), 1074251311, "Arthur Fleck's descent into madness transforms him into Gotham's infamous Joker.", "Joker.jpg", [drama, thriller]),
        ("Dune", date(2021, 10, 22), 402027830, "Paul Atreides journeys to the desert planet Arrakis to protect his family and its future.", "Dune.jpg", [action, adventure, scifi]),
        ("Top Gun Maverick", date(2022, 5, 27), 1495696292, "Captain Pete Maverick Mitchell trains a new generation of elite fighter pilots.", "Top Gun Maverick.jpg", [action, drama]),
        ("Black Panther", date(2018, 2, 16), 1349926083, "T'Challa returns to Wakanda to become king while protecting his nation from powerful enemies.", "Black Panther.jpg", [action, adventure, scifi]),
        ("Doctor Strange", date(2016, 11, 4), 677796076, "A brilliant neurosurgeon discovers the mystical arts after a life-changing accident.", "Doctor Strange.jpg", [action, adventure, scifi]),
        ("Guardians of the Galaxy", date(2014, 8, 1), 773350147, "A group of unlikely heroes join forces to stop a powerful villain from destroying the galaxy.", "Guardians of the Galaxy.jpg", [action, adventure, scifi]),
        ("Spider-Man No Way Home", date(2021, 12, 17), 1921847111, "Peter Parker seeks Doctor Strange's help after his identity is revealed, leading to multiverse chaos.", "Spider-Man No Way Home.jpg", [action, adventure, scifi]),
        ("Iron Man", date(2008, 5, 2), 585796247, "Tony Stark builds a powerful suit of armour and becomes the superhero Iron Man.", "Iron Man.jpg", [action, adventure, scifi]),
        ("Captain America Civil War", date(2016, 5, 6), 1155046416, "Political pressure divides the Avengers, forcing Captain America and Iron Man onto opposing sides.", "civil War.jpg", [action, adventure]),
        ("Thor Ragnarok", date(2017, 11, 3), 865046711, "Thor races against time to stop Ragnarok and save Asgard from destruction.", "Thor Ragnarok.jpg", [action, adventure, scifi]),
        ("Frozen", date(2013, 11, 27), 1280802282, "Princess Anna sets out to find her sister Elsa, whose magical powers have trapped their kingdom in eternal winter.", "frozen.jpg", [adventure]),
        ("Moana", date(2016, 11, 23), 687228908, "A courageous young girl sails across the ocean to restore the heart of Te Fiti and save her people.", "Moana.jpg", [adventure]),
        ("Coco", date(2017, 11, 22), 814642033, "A young boy travels to the Land of the Dead to discover his family's history and follow his dream of becoming a musician.", "Coco.jpg", [adventure, drama]),
        ("Finding Nemo", date(2003, 5, 30), 940335536, "A clownfish crosses the ocean in search of his missing son, Nemo.", "Finding Nemo.jpg", [adventure]),
        ("Toy Story", date(1995, 11, 22), 394436586, "A group of toys come to life whenever humans are not around and embark on an unforgettable adventure.", "Toy Story.jpg", [adventure]),
        ("The Lion King", date(1994, 6, 24), 968511805, "Young lion Simba must overcome tragedy and reclaim his rightful place as king of the Pride Lands.", "The Lion King.jpg", [adventure, drama]),
    ]

    movies = []

    for name, release, gross, synopsis, poster, genres in movie_data:
        movie = Movie(
            movie_name=name,
            release_date=release,
            gross_collection=gross,
            synopsis=synopsis,
            movie_poster=poster,
            genres=genres
        )

        movies.append(movie)

    db.session.add_all(movies)

    review_data = [
        ("John", 5, "Amazing movie", 0),
        ("Sarah", 4, "Really enjoyable", 1),
        ("David", 5, "Great acting", 2),
        ("Emma", 5, "Loved it", 3),
        ("Alex", 4, "Worth watching", 4),
        ("James", 5, "Fantastic", 5),
        ("Sophia", 4, "Very good", 6),
        ("Liam", 5, "Excellent", 7),
        ("Noah", 4, "Interesting story", 8),
        ("Olivia", 5, "Highly recommended", 9),
        ("Mason", 4, "Good movie", 10),
        ("Isabella", 5, "One of my favourites", 11),
        ("Lucas", 4, "Enjoyed every minute", 12),
        ("Mia", 5, "Brilliant", 13),
        ("Ethan", 4, "Good effects", 14),
        ("Charlotte", 5, "Amazing visuals", 15),
        ("Benjamin", 4, "Strong storyline", 16),
        ("Amelia", 5, "Would watch again", 17),
        ("Henry", 4, "Very entertaining", 18),
        ("Harper", 5, "Excellent film", 19),
    ]

    for username, rating, comment, movie_number in review_data:
        review = Review(
            username=username,
            rating=rating,
            comment=comment,
            review_date=date.today(),
            movie=movies[movie_number]
        )

        db.session.add(review)

    db.session.commit()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "movie-hub-class-project"

    db.init_app(app)

    with app.app_context():
        db.create_all()

        if Movie.query.count() == 0:
            add_starting_movies()

    @app.route("/")
    def home():
        featured_movies = Movie.query.order_by(Movie.id.desc()).limit(4).all()

        return render_template(
            "home.html",
            page_title="Home",
            featured_movies=featured_movies
        )

    @app.route("/movies")
    def movies_page():
        search = request.args.get("search", "").strip()
        selected_genre = request.args.get("genre", "").strip()

        movies = Movie.query.order_by(Movie.movie_name.asc()).all()
        genres = Genre.query.order_by(Genre.genre_name.asc()).all()

        if search:
            movies = [
                movie for movie in movies
                if search.lower() in movie.movie_name.lower()
            ]

        if selected_genre:
            movies = [
                movie for movie in movies
                if selected_genre in [genre.genre_name for genre in movie.genres]
            ]

        return render_template(
            "movies.html",
            page_title="Browse Movies",
            movies=movies,
            genres=genres,
            search=search,
            selected_genre=selected_genre
        )

    @app.route("/movies/<int:movie_id>")
    def movie_detail(movie_id):
        movie = db.session.get(Movie, movie_id)

        if movie is None:
            abort(404)

        reviews = sorted(
            movie.reviews,
            key=lambda review: review.review_date,
            reverse=True
        )

        return render_template(
            "movie_detail.html",
            page_title=movie.movie_name,
            movie=movie,
            reviews=reviews
        )

    @app.post("/movies/<int:movie_id>/reviews")
    def add_review(movie_id):
        movie = db.session.get(Movie, movie_id)

        if movie is None:
            abort(404)

        username = request.form.get("username", "").strip()
        comment = request.form.get("comment", "").strip()

        try:
            rating = int(request.form.get("rating", 0))
        except ValueError:
            rating = 0

        if not username or not comment or rating not in [1, 2, 3, 4, 5]:
            flash(
                "Please enter your name, review, and rating from 1 to 5.",
                "error"
            )
        else:
            review = Review(
                username=username,
                rating=rating,
                comment=comment,
                movie=movie
            )

            db.session.add(review)
            db.session.commit()

            flash("Thanks! Your review has been added.", "success")

        return redirect(url_for("movie_detail", movie_id=movie.id))

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)