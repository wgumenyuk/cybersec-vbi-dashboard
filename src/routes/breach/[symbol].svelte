<script lang="ts">
    import dataset from "$lib/data/breaches_symbols.json";
    import Title from "$lib/components/Title.svelte";

    export let params; // Dynamic parameter provided by SvelteKit
	console.log(params)

    // Find breach data based on the symbol
    let breachData = dataset.find((item) => item.Symbol === params.symbol);

	console.log("Params symbol:", params.symbol);
	console.log("Loaded breachData:", breachData);

    // Debugging logs
    console.log("Params:", params);
    console.log("Loaded breachData:", breachData);

    if (!breachData) {
        console.error(`No breach data found for symbol: ${params.symbol}`);
    }
</script>

{#if breachData}
	<Title value={`Breach Details - ${breachData.Company}`} />
	<div class="flex flex-col gap-8">
		<!-- Header -->
		<div class="flex justify-between items-center">
			<h1 class="text-2xl font-bold">{breachData.Company}</h1>
			<span class="text-gray-600 dark:text-gray-400">{breachData.Date}</span>
		</div>

		<!-- KPIs -->
		<div class="grid grid-cols-2 gap-4 md:grid-cols-4">
			<div class="border rounded-md p-4">Affected People: {breachData.Affected.toLocaleString()}</div>
			<div class="border rounded-md p-4">
				Stock Change: 
				{(
					((+breachData["Post-Attack Stock Price"] - +breachData["Pre-Attack Stock Price"]) / 
					+breachData["Pre-Attack Stock Price"]) * 100
				).toFixed(2)}%
			</div>
			<div class="border rounded-md p-4">Type of Breach: {breachData.Type.join(", ")}</div>
			<div class="border rounded-md p-4">Industry: {breachData.Industry}</div>
		</div>

		<!-- Comparative Analysis -->
		<div>
			<h2 class="text-lg font-bold mb-4">Comparative Analysis</h2>
			<div class="border rounded-md p-4 mb-4">People Affected Comparison Placeholder</div>
			<div class="border rounded-md p-4">Stock Price Change Comparison Placeholder</div>
		</div>

		<!-- Stock Price Trend -->
		<div>
			<h2 class="text-lg font-bold mb-4">Stock Price Trend</h2>
			<div class="border rounded-md p-4">Stock Price Trend Placeholder</div>
		</div>

		<!-- Breach Details -->
		<div>
			<h2 class="text-lg font-bold mb-4">Breach Details</h2>
			<div class="border rounded-md p-4">
				<p><strong>Company:</strong> {breachData.Company}</p>
				<p><strong>Industry:</strong> {breachData.Industry}</p>
				<p><strong>Type:</strong> {breachData.Type.join(", ")}</p>
				<p><strong>Affected People:</strong> {breachData.Affected.toLocaleString()}</p>
				<p><strong>Pre-Attack Stock Price:</strong> ${breachData["Pre-Attack Stock Price"]}</p>
				<p><strong>Stock Price during the Attack:</strong> ${breachData["Stock Price during the Attack"]}</p>
				<p><strong>Post-Attack Stock Price:</strong> ${breachData["Post-Attack Stock Price"]}</p>
			</div>
		</div>
	</div>
{:else}
	<p class="text-center text-gray-600 dark:text-gray-400 mt-8">
		No breach data found for the selected symbol. Please check the URL or try another entry.
	</p>
{/if}
