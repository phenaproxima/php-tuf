<?php


namespace Tuf\Metadata;

use Symfony\Component\Validator\Constraints\All;
use Symfony\Component\Validator\Constraints\Collection;
use Symfony\Component\Validator\Constraints\Count;
use Symfony\Component\Validator\Constraints\NotBlank;
use Symfony\Component\Validator\Constraints\Required;
use Symfony\Component\Validator\Constraints\Type;

class SnapshotMetadata extends MetadataBase
{

    protected const TYPE = 'snapshot';

    /**
     * {@inheritdoc}
     */
    protected static function getSignedCollectionOptions(): array
    {
        $options = parent::getSignedCollectionOptions();
        $options['fields']['meta'] = new Required([
            new Type('array'),
            new Count(['min' => 1]),
            new All([
                new Collection([
                    'version' => [
                        new NotBlank(),
                        new Type(['type' => 'integer']),
                    ],
                ]),
            ]),
        ]);
        return $options;
    }
}