<script lang="ts">
	/* eslint-disable svelte/no-unused-svelte-ignore, svelte/valid-compile */
	import { onMount } from "svelte";
	import { browser } from "$app/environment";

	// Components
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

	let tourStep = $state(-1);

	const nextStep = () => {
		tourStep++;
	};

	const exitTour = () => {
		if (!browser) {
			return;
		}

		localStorage.isTourDone = true;
		tourStep = -1;
	};

	onMount(() => {
		if (!browser) {
			return;
		}

		tourStep = localStorage.isTourDone ? -1 : 0;
	});
</script>

{#if tourStep >= 0}
	<!-- svelte-ignore a11y_no_static_element_interactions, a11y_click_events_have_key_events -->
	<div
		class="absolute left-0 top-0 z-10 h-screen w-screen backdrop-blur"
		onclick={exitTour}
	></div>
{/if}

<Card class="relative flex h-16 items-center justify-between">
	<div class={["flex", "items-center", "gap-4", tourStep === 0 && "z-20"]}>
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
		<div
			class={["flex", "items-center", "gap-4", tourStep === 1 && "z-20"]}
		>
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
	</div>

	<!-- Tour (Step 1) -->
	{#if tourStep === 0}
		<Card
			class="absolute left-0 top-full z-20 flex max-w-64 translate-y-4 flex-col items-end gap-4"
		>
			<span>View your current dashboard and see navigation path.</span>
			<div class="flex items-center justify-end gap-4">
				<button
					class="dark:text-silver-300 hover:dark:text-silver-400"
					onclick={exitTour}>Skip</button
				>
				<button
					class="rounded border px-2 py-0.5 dark:border-silver-700 dark:text-silver-300 hover:dark:bg-silver-800"
					onclick={nextStep}>Next</button
				>
			</div>
		</Card>
	{/if}

	<!-- Tour (Step 2) -->
	{#if tourStep === 1}
		<Card
			class="absolute right-0 top-full z-20 flex max-w-64 translate-y-4 flex-col items-end gap-4"
		>
			<span
				>Flip through dashboards using these buttons, just like a book.</span
			>
			<button
				class="rounded border px-2 py-0.5 dark:border-silver-700 dark:text-silver-300 hover:dark:bg-silver-800"
				onclick={exitTour}>Got it</button
			>
		</Card>
	{/if}
</Card>
