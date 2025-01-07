<script lang="ts">
	import { LandPlotIcon, TrendingUpDownIcon, UsersIcon } from "lucide-svelte";

	// Types
	import type { Component } from "svelte";

	type Link = {
		href: string;
		icon: Component;
		title: string;
		description: string;
	};

	const links: Link[] = [
		{
			href: "/",
			// @ts-expect-error: `TrendingUpDownIcon` hat einen falschen Typ.
			icon: UsersIcon,
			title: "Who?",
			description: "A Look at Attackers and Targets of Cyber Attacks"
		},
		{
			href: "/",
			// @ts-expect-error: `TrendingUpDownIcon` hat einen falschen Typ.
			icon: LandPlotIcon,
			title: "How?",
			description: "Exploring Methods and Technical Targets of Attacks"
		},
		{
			href: "/what",
			// @ts-expect-error: `TrendingUpDownIcon` hat einen falschen Typ.
			icon: TrendingUpDownIcon,
			title: "What?",
			description:
				"Understanding Breaches and Their Impact on Company Stocks"
		}
	];
</script>

{#snippet link({ href, icon, title, description }: Link)}
	<a
		{href}
		class="
		flex
		w-full
		max-w-96
		select-none
		flex-col
		items-center
		gap-8
		rounded-lg
		border
		p-8
		dark:border-silver-800
		dark:bg-silver-900
		hover:dark:border-silver-700/50
		hover:dark:bg-silver-800/50
	"
	>
		<svelte:component
			this={icon}
			size="64px"
			class="dark:text-silver-400"
		/>
		<div class="flex flex-col items-center gap-4 text-center">
			<span class="text-2xl font-bold">{title}</span>
			<span class="text-lg dark:text-silver-400">{description}</span>
		</div>
	</a>
{/snippet}

<div class="flex grow flex-col items-center justify-center gap-16 pb-16">
	<div class="flex flex-col items-center gap-8 pb-8">
		<h1 class="text-7xl">CyberSecurity Breaches</h1>
		<span class="text-2xl dark:text-silver-400"
			>Breaking Down CyberSecurity Breaches and Their Financial Impact</span
		>
	</div>
	<div class="flex items-center justify-around gap-16">
		{#each links as l}
			{@render link(l)}
		{/each}
	</div>
	<span class="dark:text-silver-400">Select a dashboard to get started.</span>
</div>
