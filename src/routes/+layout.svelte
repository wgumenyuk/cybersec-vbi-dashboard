<script lang="ts">
	import "@fontsource/roboto";
	import "../app.css";

	let { children } = $props();
</script>

<div class="min-h-screen p-8">
	{@render children()}
</div>
