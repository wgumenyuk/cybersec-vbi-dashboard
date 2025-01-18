<script>
	import Title from "$components/Title.svelte";
	import Nav from "$components/Nav.svelte";
	import Breadcrumbs from "$components/Breadcrumbs.svelte";
	import Card from "$components/Card.svelte";
	import AttackIndustry from "$components/kon/AngriffsmethodenBranchen.svelte";
	import AttackMethods from "$components/kon/AttackMethods.svelte";
	import AngriffsmethodenZeit from "$components/kon/AngriffsmethodenZeit.svelte";
	import ProtocolUsage from "$components/kon/ProtocolUsage.svelte";
	import AnomalyScores from "$components/kon/AnomalyScores.svelte";
	import AngriffeProtokolle from "$components/kon/AngriffeProtokolle.svelte";
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
			<AttackIndustry />
		</Card>
		<Card class="w-full grow">
			<AttackMethods />
		</Card>
	</div>
	<div class="flex gap-8">
		<Card class="w-full grow">
			<AngriffsmethodenZeit />
		</Card>
		<Card class="w-full grow">
			<AngriffeProtokolle />
		</Card>
	</div>
	<div class="flex gap-8">
		<Card class="w-full grow">
			<AnomalyScores />
		</Card>
		<Card class="w-full grow">
			<ProtocolUsage />
		</Card>
	</div>
</div>
