fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then((response) => response.json())
  .then((data) => {
    document.querySelector("#hello").innerHTML = data.hello;
  });
