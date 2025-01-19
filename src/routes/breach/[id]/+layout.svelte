<script lang="ts">
	import { page } from "$app/state";

	// Components
	import Breadcrumbs from "$components/Breadcrumbs.svelte";
	import Nav from "$components/Nav.svelte";

	let { children } = $props();

	const { id } = page.params;
</script>

<Nav title="Breach Details" previous="/what">
	<Breadcrumbs
		nodes={[
			{
				label: "Dashboard",
				href: "/"
			},
			{
				label: "Breach Analysis",
				href: "/what"
			},
			{
				label: `Breach #${id}`,
				href: `/breach/${id}`
			}
		]}
	/>
</Nav>

<div class="flex grow gap-8">
	{@render children()}
</div>
