<script lang="ts">
	import { onMount } from "svelte";
	import { browser } from "$app/environment";

	// Components
	import { MoonIcon, SunIcon } from "lucide-svelte";

	type Theme = "dark" | "light";

	let theme = $state<Theme>();

	const toggleTheme = () => {
		theme = theme === "dark" ? "light" : "dark";
		localStorage.theme = theme;
		document.documentElement.dataset.theme = theme;
	};

	onMount(() => {
		if (!browser) {
			return;
		}

		theme = document.documentElement.dataset.theme as Theme;
	});
</script>

<button
	onclick={toggleTheme}
	class="hover:text-silver-600 hover:dark:text-silver-50"
>
	{#if theme === "light"}
		<SunIcon />
	{:else}
		<MoonIcon />
	{/if}
</button>
