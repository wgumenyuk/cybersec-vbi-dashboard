<script lang="ts">
	import type { Snippet } from "svelte";

	let {
		children,
		class: c
	}: {
		children?: Snippet;
		class?: string;
	} = $props();
</script>

<div
	class={[
		"bg-silver-100",
		"dark:bg-silver-900",
		"p-4",
		"rounded-lg",
		"border",
		"border-silver-200",
		"dark:border-silver-800",
		"shadow-sm",
		"dark:shadow-none",
		!!c && c
	]}
>
	{@render children?.()}
</div>
