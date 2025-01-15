<script lang="ts">
	import { onMount } from "svelte";

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

<div class="container">
	<!-- Heading -->
	<div class="heading">Who?</div>

	<!-- First Map: Aggressive Countries -->
	<div class="card">
		<div class="card-title">Aggressive Countries (Attackers Map)</div>
		<div class="gradient-border gradient-attackers">
			<div class="iframe-container">
				<iframe
					title="Aggressive attacking countries"
					srcdoc={MapHtmlAttackers}
				></iframe>
			</div>
		</div>
	</div>

	<!-- Second Map: Affected Countries -->
	<div class="card">
		<div class="card-title">Affected Countries (Attacked Map)</div>
		<div class="gradient-border gradient-attacked">
			<div class="iframe-container">
				<iframe title="Hit by attack countries" srcdoc={MapHtmlAttacked}
				></iframe>
			</div>
		</div>
	</div>
</div>

<style>
	/* Overall page container */
	.container {
		padding: 16px;
		background-color: #f9f9f9;
		border-radius: 8px;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	/* "Who?" heading */
	.heading {
		font-size: 2rem;
		font-weight: bold;
		color: #333;
		text-align: left;
		margin-bottom: 24px;
		position: relative;
	}

	.heading::after {
		content: "";
		display: block;
		width: 50px;
		height: 4px;
		background-color: #333;
		border-radius: 2px;
		margin-top: 8px;
	}

	/* Card design */
	.card {
		background-color: white;
		border-radius: 12px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
		padding: 16px;
		overflow: hidden;
		margin-bottom: 24px;
		position: relative;
	}

	.card-title {
		font-size: 1.25rem;
		font-weight: bold;
		margin-bottom: 8px;
		color: #333;
	}

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
