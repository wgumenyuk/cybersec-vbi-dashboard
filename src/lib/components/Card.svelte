<script lang="ts">
	import clsx from "clsx";

	// Types
	import type { Snippet } from "svelte";

	let {
		class: optionalClasses,
		children
	}: {
		class?: string;
		children: Snippet;
	} = $props();

	const cardClass = clsx(
		optionalClasses,
		"rounded-lg",
		"bg-slate-50",
		"p-8",
		"shadow-sm"
	);
</script>

<div class={cardClass}>
	{@render children()}
</div>
