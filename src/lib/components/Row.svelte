<script lang="ts">
	let { children } = $props();
</script>

<div class="flex justify-between gap-8">
	{@render children()}
</div>
