<script lang="ts">
	import { ArrowLeftIcon, ArrowRightIcon, HomeIcon } from "lucide-svelte";
	import Card from "$components/Card.svelte";
	import Theme from "$components/Theme.svelte";

	// Types
	import type { Snippet } from "svelte";

	let {
		title,
		next,
		previous,
		children
	}: {
		title: string;
		next?: string;
		previous?: string;
		children?: Snippet;
	} = $props();
</script>

<Card class="flex h-16 items-center justify-between">
	<div class="flex items-center gap-4">
		<h1 class="text-lg">{title}</h1>
		{#if children}
			<span class="h-16 w-px bg-silver-200 dark:bg-silver-800"></span>
			{@render children()}
		{/if}
	</div>
	<div class="flex items-center gap-4">
		<a href="/" class="hover:text-silver-600 hover:dark:text-silver-50">
			<HomeIcon />
		</a>
		<Theme />
		<span class="ml-2.5 mr-1 h-16 w-px bg-silver-200 dark:bg-silver-800"
		></span>
		{#if previous}
			<a
				href={previous}
				class="hover:text-silver-600 hover:dark:text-silver-50"
			>
				<ArrowLeftIcon />
			</a>
		{:else}
			<ArrowLeftIcon class="text-silver-400 dark:text-silver-500" />
		{/if}
		{#if next}
			<a
				href={next}
				class="hover:text-silver-600 hover:dark:text-silver-50"
			>
				<ArrowRightIcon />
			</a>
		{:else}
			<ArrowRightIcon class="text-silver-400 dark:text-silver-500" />
		{/if}
	</div>
</Card>
