<script lang="ts">
	import Card from "$components/Card.svelte";

	export let affectedPeople: string = "N/A"; // Placeholder
	export let stockPriceChange: string = "N/A"; // Placeholder
</script>

<div class="grid grid-cols-2 gap-4">
	<!-- Affected People KPI -->
	<Card class="flex flex-col items-center justify-center">
		<span class="text-lg font-semibold dark:text-silver-300">
			Affected People
		</span>
		<span class="text-3xl font-bold text-rose-500 dark:text-rose-400">
			{affectedPeople}
		</span>
	</Card>

	<!-- Stock Price Change KPI -->
	<Card class="flex flex-col items-center justify-center">
		<span class="text-lg font-semibold dark:text-silver-300">
			Stock Price Change (%)
		</span>
		<span class="text-3xl font-bold text-emerald-500 dark:text-emerald-400">
			{stockPriceChange}
		</span>
	</Card>
</div>
