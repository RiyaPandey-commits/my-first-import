import { useState } from 'react'
import MovieCard from '../components/MovieCard'
import '../css/Home.css'
import '../css/MovieCard.css'

function Home() {

    const [searchQuery, setSearchQuery] = useState("");

    const movies = [
        {id:1, title:"Dada", release_date:"2023"},
        {id:2, title:"OMK", release_date:'2022'},
        {id:3, title:"Money Heist", release_date:'2015'},
        {id:4, title:"VTV", release_date: '2010'},
        {id:5, title:"Sachin", release_date:'2019'},
        {id:6, title:"Stranger Things", release_date:'2015'},
        {id:7, title: "Wednesday", release_date: '2010'}
    ]

    const onHandleSubmit = (e) => {
        e.preventDefault();
        alert(searchQuery)
        setSearchQuery("");
    }

  return (
    <div className="home">
        <form onSubmit={onHandleSubmit} className='search-form'>
            <input 
             type="text"
             placeholder='Search for movies..' 
             className='search-bar'
             value={searchQuery}
             onChange={(e) => setSearchQuery(e.target.value)}
             />
            <button type='submit' className='search-btn'>Search</button>
        </form>
        <div className="movies-grid">
            {movies.map((movie) => movie.title.toLowerCase().startsWith(searchQuery) && (
                <MovieCard movie={movie} key={movie.id}/>
            ))}
        </div>
    </div>
  )
}

export default Home