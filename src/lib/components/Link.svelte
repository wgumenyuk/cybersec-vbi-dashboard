<script lang="ts">
	import { ExternalLinkIcon } from "lucide-svelte";

	// Types
	import type { Snippet } from "svelte";

	let {
		href,
		children
	}: {
		href: string;
		children: Snippet;
	} = $props();
</script>

<a
	{href}
	class="flex w-fit border-spacing-2 items-center gap-1.5 border-b border-dotted border-slate-500"
>
	{@render children()}
	<ExternalLinkIcon size="16px" />
</a>
