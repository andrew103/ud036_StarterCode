import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
					 "A marine goes on an adventure",
					 "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
					 
doctor_strange = media.Movie("Doctor Strange",
							 "A doctor with extraordinary powers",
							 "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Doctor_Strange_poster.jpg/220px-Doctor_Strange_poster.jpg",
							 "https://www.youtube.com/watch?v=HSzx-zryEgM")

das_boot = media.Movie("Das Boot",
					   "A story of a german U-boat in hostile seas",
					   "https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Das_boot_ver1.jpg/220px-Das_boot_ver1.jpg",
					   "https://www.youtube.com/watch?v=FRKXemPhtYI")
					   
pacific_rim = media.Movie("Pacific Rim",
						  "Giant robots fight aliens from the sea",
						  "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Pacific_Rim_FilmPoster.jpeg/220px-Pacific_Rim_FilmPoster.jpeg",
						  "www.youtube.com/watch?v=-hNVKNFsyu0")
						  
avengers = media.Movie("Avengers",
					   "A team of superheroes fight evil",
					   "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",
					   "https://www.youtube.com/watch?v=eOrNdBpGMv8")

wargames = media.Movie("WarGames",
					   "A game is played with AI",
					   "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Wargames.jpg/220px-Wargames.jpg",
					   "https://www.youtube.com/watch?v=tAcEzhQ7oqA")

					   
movies = [avatar, doctor_strange, das_boot, pacific_rim, avengers, wargames]

fresh_tomatoes.open_movies_page(movies)