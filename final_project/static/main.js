$(document).ready(() => {
    $('#searchForm').on('submit', (event) => {
        let searchText = ($('#searchText').val());
        getMovies(searchText);
        event.preventDefault();
    })

});



function getMovies(searchText){
    axios.get('http://www.omdbapi.com/?s='+ searchText +'&apikey=4336f4f8&r=json')
    .then((response) => {
        console.log(response);
        let movies = response.data.Search;
        let output = '';
        //this is a loop that loops through all the movies included by search keyword 'searchText'
        $.each(movies, (index, movie) => {
            output += `
                <div class="col-md-3">
                    <div class="well text-center">
                        <img src="${movie.Poster}">
                        <h5>${movie.Title}</h5>
                        <a onclick="movieSelected('${movie.imdbID}')" 
                        class="btn btn-primary" href="#">More</a>
                    </div>
                </div>
            `;
        });
        
        $('#movies').html(output);
    })
    .catch((err) => {
        console.log(err);
    });


}

function movieSelected(id){
    // saves id
    sessionStorage.setItem('movieId', id);
    // changing the page to movie.html
    window.location = 'movie';
    return false;
}

function getMovie(){
    let movieId = sessionStorage.getItem('movieId');
    axios.get('http://www.omdbapi.com/?i='+ movieId +'&apikey=4336f4f8&r=json')
    .then((response) => {
        console.log(response);
        let movie = response.data;

        output = `
            <div class="row">
                <div class="col-md-4">
                    <img src="${movie.Poster}" class="thumbnail">
                </div>
                <div class="col-md-8">
                    <h2>${movie.Title}</h2>
                    <ul class="list-group">
                        <li class="list-group-item">Genre: ${movie.Genre} </li>
                        <li class="list-group-item">Released: ${movie.Released} </li>
                        <li class="list-group-item">Rated: ${movie.Rated} </li>
                        <li class="list-group-item">IMDB Rating: ${movie.imdbRating} </li>
                        <li class="list-group-item">Director: ${movie.Director} </li>
                        <li class="list-group-item">Writer: ${movie.Writer} </li>
                        <li class="list-group-item">Actors: ${movie.Actors} </li>
                    </ul>
                </div>
            </div>
            <div class="row">
                <div class="well">
                    <h3>Plot</h3>
                    ${movie.Plot}
                    <hr>
                    <a href="https://imdb.com/title/${movie.imdbID}" target="_blank" class="btn btn-primary">View IMDB</a>
                    <a href="http://127.0.0.1:5000/post/new" target="_blank" class="btn btn-primary">Comment</a>
                    <a href="index.html" class="btn btn-default">Go Back to Search</a>
                </div>
            </div>
        `

        //this line inserts 'output' inside a html tag whos id='movie'
        $('#movie').html(output);
        
    })
    .catch((err) => {
        console.log(err);
    });
}

