function getRandomGreeting() {
	const greetings = [
		"Hello!",
		"Hi there!",
		"Greetings!",
		"Hey!",
		"Howdy!",
		"Welcome!",
		"Good day!"
	];
	const index = Math.floor(Math.random() * greetings.length);
	return greetings[index];
}
// A function that returns a random greeting
