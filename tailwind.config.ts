import typography from "@tailwindcss/typography";

// Types
import type { Config } from "tailwindcss";

export default {
	content: ["./src/**/*.{html,js,svelte,ts}"],
	plugins: [typography],
	theme: {
		extend: {}
	}
} satisfies Config;
