<script>
	import Title from "$components/Title.svelte";
	import Nav from "$components/Nav.svelte";
	import Breadcrumbs from "$components/Breadcrumbs.svelte";
	import Card from "$components/Card.svelte";
	import AttackIndustry from "$components/kon/AngriffsmethodenBranchen.svelte";
	import AttackMethods from "$components/kon/AttackMethods.svelte";
	import AngriffsmethodenZeit from "$components/kon/AngriffsmethodenZeit.svelte";
	import AnomalyScores from "$components/kon/AnomalyScores.svelte";
	import AngriffeProtokolle from "$components/kon/AngriffeProtokolle.svelte";
	import ActionTaken from "$components/kon/ActionTaken.svelte";
</script>

<Title value="Attack Method Analysis" />

<Nav title="Attack Method Analysis" previous="/who" next="/what">
	<Breadcrumbs
		nodes={[
			{
				label: "Dashboard",
				href: "/"
			},
			{
				label: "Attack Methods",
				href: "/how"
			}
		]}
	/>
</Nav>

<div class="flex flex-col gap-8">
	<div class="flex gap-8">
		<Card class="w-full grow">
			<span class="text-center dark:text-silver-400"
				>Attack Types and Industries</span
			>
			<AttackIndustry />
		</Card>
		<Card class="w-full grow">
			<span class="text-center dark:text-silver-400">Attack Types</span>
			<AttackMethods />
		</Card>
	</div>
	<div class="flex gap-8">
		<Card class="w-full grow">
			<span class="text-center dark:text-silver-400"
				>Attacks Over Time</span
			>
			<AngriffsmethodenZeit />
		</Card>
		<Card class="w-full grow">
			<span class="text-center dark:text-silver-400"
				>Attacks Frequency by Protocols Used and Complexity</span
			>
			<AngriffeProtokolle />
		</Card>
	</div>
	<div class="flex gap-8">
		<Card class="h-[768px] w-full">
			<span class="text-center dark:text-silver-400">Anomaly Scores</span>
			<AnomalyScores />
		</Card>
		<Card class="w-full grow">
			<span class="text-center dark:text-silver-400"
				>Actions Taken Against Attacks</span
			>
			<ActionTaken />
		</Card>
	</div>
</div>
