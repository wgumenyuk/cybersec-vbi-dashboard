<script lang="ts">
	// Components
	import Nav from "$components/Nav.svelte";
	import Breadcrumbs from "$components/Breadcrumbs.svelte";
	import Card from "$components/Card.svelte";

	// Import the HTML files
	import MapHtmlAttackers from "$lib/map/attacker_heatmap.html?raw";
	import MapHtmlAttacked from "$lib/map/attacked_heatmap.html?raw";

	// Import the KPI JSON
	import KpiData from "$lib/map/kpi_data.json";
</script>

<Nav title="Attackers and Defenders" next="/how">
	<Breadcrumbs
		nodes={[
			{
				label: "Dashboard",
				href: "/"
			},
			{
				label: "Attackers and Defenders",
				href: "/who"
			}
		]}
	/>
</Nav>

<div class="flex gap-8">
	<!-- KPIs -->
	<div class="flex flex-col gap-8">
		<Card class="min-w-64 grow">
			<h2>Total Attacks</h2>
			<p class="kpi-value kpi-attackers">{KpiData["Total Attacks"]}</p>
		</Card>
		<Card class="min-w-64 grow">
			<h2>Total Countries Involved</h2>
			<p class="kpi-value">{KpiData["Total Countries Involved"]}</p>
		</Card>
		<Card class="min-w-64 grow">
			<h2>Top Attacking Country</h2>
			<p class="kpi-value kpi-attackers">
				{KpiData["Top Attacking Country"].Country} ({KpiData[
					"Top Attacking Country"
				].Attacks} Attacks)
			</p>
		</Card>
		<Card class="min-w-64 grow">
			<h2>Top Attacked Country</h2>
			<p class="kpi-value kpi-attacked">
				{KpiData["Top Attacked Country"].Country} ({KpiData[
					"Top Attacked Country"
				].Attacks} Attacks)
			</p>
		</Card>
	</div>

	<!-- First Map: Aggressive Countries -->
	<Card class="flex grow flex-col gap-4">
		<span class="dark:text-silver-400"
			>Aggressive Countries (Attackers Map)</span
		>
		<div class="gradient-border gradient-attackers">
			<div class="iframe-container">
				<iframe
					title="Aggressive attacking countries"
					srcdoc={MapHtmlAttackers}
				></iframe>
			</div>
		</div>
	</Card>
</div>

<!-- Second Map: Affected Countries -->
<Card class="flex flex-col gap-4">
	<span class="dark:text-silver-400">Affected Countries (Attacked Map)</span>
	<div class="gradient-border gradient-attacked">
		<div class="iframe-container">
			<iframe title="Hit by attack countries" srcdoc={MapHtmlAttacked}
			></iframe>
		</div>
	</div>
</Card>

<style>
	/* Gradient border wrapper */
	.gradient-border {
		padding: 4px;
		border-radius: 12px;
		background: linear-gradient(
			135deg,
			var(--gradient-start),
			var(--gradient-end)
		);
	}

	/* Inner iframe container */
	.iframe-container {
		border-radius: 12px;
		overflow: hidden;
		background: white; /* Ensure clean contrast inside */
	}

	.iframe-container iframe {
		width: 100%;
		height: 600px;
		border: none;
	}

	/* KPI Value Styling */
	.kpi-value {
		font-size: 1.8rem;
		font-weight: bold;
		margin-top: 8px;
	}

	.kpi-attackers {
		color: #ff4757; /* Matches the attackers map gradient */
	}

	.kpi-attacked {
		color: #1e90ff; /* Matches the attacked map gradient */
	}

	/* Custom gradients for each map */
	:root {
		--attackers-gradient-start: #ff4757;
		--attackers-gradient-end: #ffa502;

		--attacked-gradient-start: #1e90ff;
		--attacked-gradient-end: #8a2be2;
	}

	/* Assign dynamic gradients */
	.gradient-attackers {
		--gradient-start: var(--attackers-gradient-start);
		--gradient-end: var(--attackers-gradient-end);
	}

	.gradient-attacked {
		--gradient-start: var(--attacked-gradient-start);
		--gradient-end: var(--attacked-gradient-end);
	}
</style>
