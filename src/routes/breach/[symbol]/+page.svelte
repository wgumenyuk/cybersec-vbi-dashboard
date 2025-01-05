<script lang="ts">
	import Title from "$components/Title.svelte";
	import Card from "$components/Card.svelte";
	import dataset from "$lib/data/breaches_symbols.json";

	export let params;

	let breachData = dataset.find((item) => item.Symbol === params.symbol);

	if (!breachData) {
		console.error("No breach data found for symbol:", params.symbol);
	}
</script>

{#if breachData}
	<Title value={`Breach Details - ${breachData.Company}`} />
	<Card>
		<h1>{breachData.Company}</h1>
		<p>Symbol: {breachData.Symbol}</p>
		<p>Industry: {breachData.Industry}</p>
		<p>Date: {breachData.Date}</p>
		<p>Type: {breachData.Type.join(", ")}</p>
		<p>Affected: {breachData.Affected}</p>
	</Card>
{:else}
	<p>Loading breach details...</p>
{/if}
