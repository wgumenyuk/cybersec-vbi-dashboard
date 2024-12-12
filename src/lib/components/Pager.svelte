<script lang="ts">
	import { ChevronLeftIcon, ChevronRightIcon } from "lucide-svelte";

	// Internal
	import { goto } from "$app/navigation";

	type Props = {
		previous?: string;
		next?: string;
	};

	let { previous, next }: Props = $props();
</script>

{#snippet button(href: string | null, isLeft: boolean)}
	<button
		class="absolute top-1/2 grid h-24 w-fit -translate-y-1/2 place-content-center rounded-r bg-slate-50 p-2 text-slate-500 shadow"
		class:left-0={isLeft}
		class:right-0={!isLeft}
		class:hidden={href === null}
		onclick={() => href && goto(href)}
	>
		{#if isLeft}
			<ChevronLeftIcon />
		{:else}
			<ChevronRightIcon />
		{/if}
	</button>
{/snippet}

{@render button(previous || null, true)}
{@render button(next || null, false)}
