import requests
import json

def search_movie(search_string):
	url = "https://api.themoviedb.org/3/search/movie"
	url_dict = {
		'api_key':'c642a0681a875a49d18b1733628b6a5a',
		'language':'en-US',
		'query':search_string,
		'page':1,
		'include_adult':'false'
	}

	response = requests.request("GET", url, params=url_dict)
	out = response.text
	return json.loads(out)['results']

def format_data(movie_details, gen_dict):
    for item in movie_details:
        item['genre_ids'] = find_genre(item['genre_ids'], gen_dict)
        item['release_date'] = get_release_year(item['release_date'])
        item['poster_path'] = generate_poster(item['poster_path'])
    return movie_details

def get_genre_dict():
	# get genre json file
	url = "https://api.themoviedb.org/3/genre/movie/list?api_key=c642a0681a875a49d18b1733628b6a5a&language=en-US"
	response = requests.request("GET", url)
	out_genre = json.loads(response.text)['genres']

	genre_dict = {}
	for item in out_genre:
	  genre_dict[item['id']] = item['name']
	return genre_dict

def find_genre(id_list, genre_dict):
    genre_list = []
    for id in id_list:
      genre_list.append(genre_dict[id])
    return genre_list

def generate_poster(image_url):
	if image_url:
		poster_url = 'https://image.tmdb.org/t/p/w500' + image_url
		return poster_url
    # response = requests.get(poster)
    # img = Image.open(io.BytesIO(response.content))
    # img = plt.imshow(img)
    # img = plt.show()
	else:
		return ""

def get_release_year(release_date):
  extracted_year = 'not provided' if not release_date else release_date[:4]
  return extracted_year

# Extract the movie information
# values_ = {'title':'Title: ', 'overview':'Overview: ','original_language':'Original Language: ','vote_average':'Score: '}
# for i, item in enumerate(movie_details):
#     for d_ in values_:
#       print("{} {}".format(values_.get(d_), item[d_]))
#     print("Genre: {}".format(find_genre(item['genre_ids'], genre_dict)))
#     print("Release_Year: {}".format(get_release_year(item['release_date'])))
