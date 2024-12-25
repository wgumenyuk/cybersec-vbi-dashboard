<script lang="ts">
	import "@fontsource/roboto";
	import "../app.css";

	let { children } = $props();
</script>

<svelte:head>
	<script>
		const prefersDark =
			localStorage.theme === "dark" ||
			(!("theme" in localStorage) &&
				window.matchMedia("(prefers-color-scheme: dark)").matches);

		document.documentElement.dataset.theme = prefersDark ? "dark" : "light";
	</script>
</svelte:head>

<div class="mx-auto flex h-screen max-w-[1920px] flex-col gap-8 p-8">
	{@render children()}
</div>
