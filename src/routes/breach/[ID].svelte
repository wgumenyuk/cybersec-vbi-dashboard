<script lang="ts">
	import Card from "$components/Card.svelte";
	import { page } from "$app/stores";
	import Nav from "$components/Nav.svelte"

	// Variables to store ID
	let id: string = "";

	// Reactive declaration to extract ID
	$: {
		id = $page.params.id; // Extract ID from URL
	}

	// Dummy data for demonstration
	let breachData = {
		Company: "Unknown",
		ID: id,
	};

	// In a real-world scenario, fetch breach data here based on ID
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

<!-- Breach Details -->
<Card>
	<h2 class="text-xl font-bold">Breach #{breachData.ID}</h2>
	<p class="text-silver-600">Company: {breachData.Company}</p>
</Card>
