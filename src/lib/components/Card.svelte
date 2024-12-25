<script lang="ts">
	import clsx from "clsx";

	// Types
	import type { Snippet } from "svelte";

	let {
		children,
		class: oc
	}: {
		children?: Snippet;
		class?: string;
	} = $props();

	const c = clsx(
		oc,
		"bg-silver-100",
		"dark:bg-silver-900",
		"p-4",
		"rounded-lg",
		"border",
		"border-silver-200",
		"dark:border-silver-800",
		"shadow-sm",
		"dark:shadow-none"
	);
</script>

<div class={c}>
	{@render children?.()}
</div>
