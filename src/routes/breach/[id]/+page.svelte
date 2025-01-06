<script lang="ts">
	import Card from "$components/Card.svelte";
	import { page } from "$app/stores";
	import Nav from "$components/Nav.svelte";
	import dataset from "$lib/data/breaches_symbols.json"; // Import the dataset

	// Define the type for your dataset rows
	type BreachData = {
		ID: number;
		Company: string;
		Symbol: string;
		Date: string;
		Industry: string;
		Type: string[];
		Affected: number | string;
		Pre?: number | string;
		Post?: number | string;
		During?: number | string;
	};

	let id: number = 0; // ID as a number
	let breachData: BreachData | null = null; // Explicit type for breachData

	// Extract ID from route params and find matching row
	$: {
		id = parseInt($page.params.id); // Parse ID as number
		breachData = dataset.find((item) => item.ID === id) || null;
	}

	// Calculate stock prices and percentage change
	let stockPriceBefore = 0;
	let stockPriceAfter = 0;
	let percentageChange = "N/A";

	$: {
		if (breachData) {
			stockPriceBefore = breachData.Pre ? parseFloat(breachData.Pre as string) : 0;
			stockPriceAfter = breachData.Post ? parseFloat(breachData.Post as string) : 0;
			percentageChange = calculatePercentageChange(stockPriceBefore, stockPriceAfter);
		}
	}

	function calculatePercentageChange(before: number, after: number): string {
		if (before === 0) return "N/A"; // Avoid division by zero
		const change = ((after - before) / before) * 100;
		return `${change > 0 ? "+" : ""}${change.toFixed(2)}%`;
	}
</script>

<Nav title="Breach Details">
	<!-- Back Button -->
	<button
		type="button"
		class="text-silver-500 hover:underline"
		on:click={() => history.back()}
	>
		&larr; Back
	</button>
</Nav>

{#if breachData}
	<!-- Flex Container for KPIs -->
	<div class="flex flex-wrap justify-between gap-4 mb-8">
		<!-- Company Name KPI -->
		<Card class="flex flex-col items-center justify-center flex-grow">
			<h3 class="text-lg font-semibold text-silver-600">Company</h3>
			<p class="text-xl font-bold">{breachData.Company}</p>
		</Card>

		<!-- Company Symbol KPI -->
		<Card class="flex flex-col items-center justify-center flex-grow">
			<h3 class="text-lg font-semibold text-silver-600">Symbol</h3>
			<p class="text-xl font-bold">{breachData.Symbol}</p>
		</Card>

		<!-- Breach Date KPI -->
		<Card class="flex flex-col items-center justify-center flex-grow">
			<h3 class="text-lg font-semibold text-silver-600">Date</h3>
			<p class="text-xl font-bold">{breachData.Date}</p>
		</Card>
	</div>

	<div class="flex flex-col items-center justify-center flex-grow">
		<!-- Industry KPI -->
		<Card class="flex flex-col items-center justify-center flex-grow">
			<h3 class="text-lg font-semibold text-silver-600">Industry</h3>
			<p class="text-xl font-bold">{breachData.Industry}</p>
		</Card>

		<!-- Breach Type KPI -->
		<Card class="flex flex-col items-center justify-center flex-grow">
			<h3 class="text-lg font-semibold text-silver-600">Type</h3>
			<p class="text-xl font-bold">{breachData.Type.join(", ")}</p>
		</Card>

		<!-- # of affected People KPI -->
		<Card class="flex flex-col items-center justify-center flex-grow">
			<h3 class="text-lg font-semibold text-silver-600">Affected</h3>
			<p class="text-xl font-bold">{breachData.Affected}</p>
		</Card>

		<!-- Stock Price Change KPI -->
		<Card class="flex flex-col items-center justify-center flex-grow">
			<h3 class="text-lg font-semibold text-silver-600">Price Change in %</h3>
			<p class="text-xl font-bold">{percentageChange}</p>
		</Card>
	</div>

	<!-- Additional Details -->
	<Card>
		<h2 class="text-xl font-bold">Breach #{breachData.ID}</h2>
		<p>Industry: {breachData.Industry}</p>
		<p>Type: {breachData.Type.join(", ")}</p>
		<p>Affected: {breachData.Affected}</p>
	</Card>
{:else}
	<p>No data found for this breach.</p>
{/if}