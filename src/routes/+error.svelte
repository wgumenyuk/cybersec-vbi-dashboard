<script lang="ts">
	import { page } from "$app/stores";

	const messages: Record<number, string> = {
		404: "This page doesn't seem to exist.",
		500: "An unexpected error occurred."
	};
</script>

<div class="grid grow place-content-center gap-4">
	<h1 class="text-8xl">{$page.status}</h1>
	<span class="text-2xl dark:text-silver-400">{messages[$page.status]}</span>
	<a
		href="/"
		class="mt-12 rounded-lg border px-4 py-2.5 text-center dark:border-silver-700 hover:dark:bg-silver-800"
		>Return to homepage</a
	>
</div>
