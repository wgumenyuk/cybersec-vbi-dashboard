<script lang="ts">
	import { onMount } from "svelte";

	// Components
	import Nav from "$components/Nav.svelte";
	import Breadcrumbs from "$components/Breadcrumbs.svelte";
	import Card from "$components/Card.svelte";

	// Import the HTML files
	import MapHtmlAttackers from "$lib/map/cybersecurity_map.html?raw";
	import MapHtmlAttacked from "$lib/map/destination_countries_map_vulnerability.html?raw";

	onMount(() => {
		// Listen for messages from iframes (if needed in the future)
		window.addEventListener("message", handleMapMessage);

		return () => {
			window.removeEventListener("message", handleMapMessage);
		};
	});

	function handleMapMessage() {
		// Placeholder for processing messages if required
	}
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
		<Card class="min-w-64 grow">…</Card>
		<Card class="min-w-64 grow">…</Card>
		<Card class="min-w-64 grow">…</Card>
		<Card class="min-w-64 grow">…</Card>
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
