<script>
	let random = 'Click the button!';

	function getRandom() {
		fetch('/api/random')
			.then((res) => res.text())
			.then((output) => (random = output));
	}
</script>

<h1>{random}</h1>
<button on:click={getRandom}>Get a random integer!</button>
