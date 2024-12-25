<script lang="ts">
	import { ExternalLinkIcon } from "lucide-svelte";

	// Types
	import type { Snippet } from "svelte";

	let {
		href,
		children
	}: {
		href: string;
		children?: Snippet;
	} = $props();
</script>

<a
	{href}
	class="flex w-fit items-center gap-1.5 border-b border-dotted border-silver-800 hover:border-silver-500 dark:border-silver-400 hover:dark:border-silver-100"
>
	<span>
		{@render children?.()}
	</span>
	<ExternalLinkIcon size="18px" />
</a>
