/**
 * The Ochrelle "Pigment Chip" mark, drawn from scratch for this project.
 * An ochre chip with a concave quarter-circle bite at the top right and a
 * floating pigment dot in the bite. Used in the site header, footer, legal
 * pages, and as the favicon (src/app/icon.svg).
 *
 * maskId must be unique per document when more than one instance renders on
 * the same page.
 */
export function PigmentChip({
  size = 17,
  maskId = "ochrelle-chip",
}: {
  size?: number;
  maskId?: string;
}) {
  return (
    <svg
      viewBox="0 0 24 24"
      width={size}
      height={size}
      aria-hidden="true"
      className="shrink-0"
    >
      <mask id={maskId}>
        <rect width="24" height="24" fill="#fff" />
        <circle cx="19" cy="5" r="6.5" fill="#000" />
      </mask>
      <rect
        x="2"
        y="4"
        width="17"
        height="16"
        rx="3.5"
        fill="#C2410C"
        mask={`url(#${maskId})`}
      />
      <circle cx="20.6" cy="3.4" r="2.7" fill="#FAFAF9" />
    </svg>
  );
}
