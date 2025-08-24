const API_KEY = "a6d9b1cbd313cd101790ae1e106b815a";
const BASE_URL = "https://www.themoviedb.org/settings/api";


export const getPopularMovies = async () => {
    const response = await fetch(`${BASE_URL}/movie/popular?api_key=${API_KEY}`);
    const data = await response.json();
    return data.results
}