<script lang="ts">
	import { ChevronRightIcon } from "lucide-svelte";

	type Node = {
		label: string;
		href?: string;
	};

	let {
		nodes
	}: {
		nodes: Node[];
	} = $props();
</script>

<div class="flex items-center gap-0.5">
	{#each nodes as node, i}
		{#if node.href}
			<a href={node.href} class="text-silver-500 dark:text-silver-400"
				>{node.label}</a
			>
		{:else}
			<span class="text-silver-500 dark:text-silver-400"
				>{node.label}</span
			>
		{/if}

		{#if i < nodes.length - 1}
			<ChevronRightIcon size="16px" />
		{/if}
	{/each}
</div>
