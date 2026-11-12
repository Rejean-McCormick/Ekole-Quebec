<?php
// This file is a candidate addition to local/uckk/classes/local/kristal/.
// It does not write anything to Moodle and is not installed automatically.
namespace local_uckk\local\kristal;

defined('MOODLE_INTERNAL') || die();

/**
 * Validated, read-only consumer of Ekole's candidate Kristal projection plan.
 * Semantic authority remains with Kristal. Operational authority remains with Moodle.
 *
 * @package local_uckk
 */
final class projection_plan_reader {
    /**
     * Load a trusted operator-configured path, never a path supplied by HTTP clients.
     *
     * @param string $filename Absolute file path outside public webroot.
     * @return array<string, mixed>
     */
    public static function load(string $filename): array {
        if (!is_file($filename) || !is_readable($filename)) {
            throw new \RuntimeException('Kristal projection plan unavailable');
        }
        $content = file_get_contents($filename);
        if ($content === false) {
            throw new \RuntimeException('Unable to read Kristal projection plan');
        }
        $plan = json_decode($content, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($plan) || ($plan['format'] ?? null) !== 'ekole.kristal-moodle-projection-plan/1.0'
            || ($plan['dry_run'] ?? null) !== true || ($plan['write_authorized'] ?? null) !== false
            || ($plan['plugin_owner'] ?? null) !== 'local_uckk'
            || !is_array($plan['kristal_projections'] ?? null)
            || !is_array($plan['relations'] ?? null)) {
            throw new \UnexpectedValueException('Unsupported or unsafe Kristal projection plan');
        }
        $ids = [];
        foreach ($plan['kristal_projections'] as $projection) {
            if (!is_array($projection) || !is_string($projection['kristal_id'] ?? null)
                || !is_string($projection['state_ref'] ?? null) || !is_array($projection['semantic_state'] ?? null)
                || !is_array($projection['moodle_projection'] ?? null)
                || ($projection['semantic_state']['does_moodle_own_semantics'] ?? null) !== false
                || ($projection['moodle_projection']['mode'] ?? null) !== 'read_only_dry_run'
                || ($projection['moodle_projection']['automatic_grade_import'] ?? null) !== false
                || ($projection['moodle_projection']['automatic_course_creation'] ?? null) !== false) {
                throw new \UnexpectedValueException('Malformed or dangerous Kristal projection');
            }
            $id = $projection['kristal_id'];
            if (isset($ids[$id])) {
                throw new \UnexpectedValueException('Duplicate Kristal projection');
            }
            $ids[$id] = true;
        }
        foreach ($plan['relations'] as $relation) {
            if (!is_array($relation) || ($relation['automatic_restriction'] ?? null) !== false) {
                throw new \UnexpectedValueException('Moodle automatic restriction is forbidden');
            }
        }
        return $plan;
    }

    /**
     * Return a single candidate by semantic identity; does not query Moodle DB.
     *
     * @param array<string, mixed> $plan Validated plan from load().
     * @param string $kristalid Local Kristal id.
     * @return array<string, mixed>|null
     */
    public static function candidate(array $plan, string $kristalid): ?array {
        foreach ($plan['kristal_projections'] as $projection) {
            if ($projection['kristal_id'] === $kristalid) {
                return $projection;
            }
        }
        return null;
    }
}
