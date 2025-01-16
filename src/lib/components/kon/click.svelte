<script>
	import AttackMethods from "$components/kon/AttackMethods.svelte";
	import BreachByYear from "$components/kon/BreachByYear.svelte";
	import AffectedSectors from "$components/kon/AffectedSectors.svelte";
	import SeverityLevels from "$components/kon/SeverityLevels.svelte";
	import RecordDistribution from "$components/kon/RecordDistribution.svelte";
	import AnomalyScores from "$components/kon/AnomalyScores.svelte";
	import AngriffsmethodenBranchen from "./AngriffsmethodenBranchen.svelte";
	import AngriffsmethodenZeit from "./AngriffsmethodenZeit.svelte";
	import AngriffeProtokolle from "./AngriffeProtokolle.svelte";
	import ProtocolUsage from "./ProtocolUsage.svelte";

	let activeTab = $state("AttackMethods");
</script>

<div>
	<div class="tab-buttons">
		<button
			class:active={activeTab === "AttackMethods"}
			onclick={() => (activeTab = "AttackMethods")}>Attack Methods</button
		>
		<button
			class:active={activeTab === "BreachByYear"}
			onclick={() => (activeTab = "BreachByYear")}>Breach By Year</button
		>
		<button
			class:active={activeTab === "AffectedSectors"}
			onclick={() => (activeTab = "AffectedSectors")}
			>Affected Sectors</button
		>
		<button
			class:active={activeTab === "SeverityLevels"}
			onclick={() => (activeTab = "SeverityLevels")}
			>Severity Levels</button
		>
		<button
			class:active={activeTab === "RecordDistribution"}
			onclick={() => (activeTab = "RecordDistribution")}
			>Record Distribution</button
		>
		<button
			class:active={activeTab === "AnomalyScores"}
			onclick={() => (activeTab = "AnomalyScores")}>Anomaly Scores</button
		>
		<button
			class:active={activeTab === "AngriffeProtokolle"}
			onclick={() => (activeTab = "AngriffeProtokolle")}
			>Angriffe Protokolle</button
		>
		<button
			class:active={activeTab === "AngriffsmethodenZeit"}
			onclick={() => (activeTab = "AngriffsmethodenZeit")}
			>Angriffe Zeit</button
		>
		<button
			class:active={activeTab === "AngriffsmethodenBranchen"}
			onclick={() => (activeTab = "AngriffsmethodenBranchen")}
			>Angriffe Branchen</button
		>
	</div>

	<div class="tab-content">
		{#if activeTab === "AttackMethods"}
			<AttackMethods />
		{/if}
		{#if activeTab === "BreachByYear"}
			<BreachByYear />
		{/if}
		{#if activeTab === "AffectedSectors"}
			<AffectedSectors />
		{/if}
		{#if activeTab === "SeverityLevels"}
			<SeverityLevels />
		{/if}
		{#if activeTab === "ProtocolUsage"}
			<ProtocolUsage />
		{/if}
		{#if activeTab === "RecordDistribution"}
			<RecordDistribution />
		{/if}
		{#if activeTab === "AnomalyScores"}
			<AnomalyScores />
		{/if}
		{#if activeTab === "AngriffeProtokolle"}
			<AngriffeProtokolle />
		{/if}
		{#if activeTab === "AngriffsmethodenZeit"}
			<AngriffsmethodenZeit />
		{/if}
		{#if activeTab === "AngriffsmethodenBranchen"}
			<AngriffsmethodenBranchen />
		{/if}
	</div>
</div>

<!-- svelte-ignore css_unused_selector -->
<style>
	.tab-buttons {
		display: flex;
		justify-content: space-around;
		margin-bottom: 1rem;
	}

	.tab-buttons button {
		padding: 0.5rem 1rem;
		border: none;
		cursor: pointer;
		background-color: #007bff;
		color: white;
		border-radius: 4px;
	}

	.tab-buttons button.active {
		background-color: #0056b3;
	}

	.tab-content {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 500px;
		overflow: hidden;
	}

	canvas {
		max-width: 100%;
		max-height: 100%;
		height: auto;
		width: auto;
	}
</style>
