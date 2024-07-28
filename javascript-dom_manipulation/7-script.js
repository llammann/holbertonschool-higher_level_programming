fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => response.json())
  .then((data) => {
    data.results.forEach((movie) => {
      document.querySelector("ul#list_movies").innerHTML =
        document.querySelector("ul#list_movies").innerHTML +
        `<li>${movie.title}</li>`;
    });
  });
