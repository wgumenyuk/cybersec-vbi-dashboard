<script lang="ts">
	let { children } = $props();
</script>

<div class="rounded-lg bg-slate-50 p-4 shadow-sm">
	{@render children()}
</div>
