window.onload = async function load() {
  getExercises();
};

async function getExercises() {
  host = "http://127.0.0.1:5000/stories";
  const result = await fetch(host, {
    method: "GET",
    credentials: "include",
  });
  const data = await result.json();
  displayExercises(data.exercises);
}

function displayExercises(exercises) {
  exercises.forEach(createExercise);
}

function createExercise(exercise) {
  const exercises = document.getElementById("exercises");
  const exerciseWrapper = document.createElement("div");
  exerciseWrapper.innerHTML = `
    <p>
        <a class="name"> ${exercise.name} </a>
        <span>(hi)</span>
    </p>`;
  exercises.append(exerciseWrapper);
}
