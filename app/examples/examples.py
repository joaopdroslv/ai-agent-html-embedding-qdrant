from app.schemas.category import Category
from app.schemas.request_embedding import RequestEmbedding

general_questions_category = Category(
    id=1,
    name="General Questions",
    description="Questions about general topics.",
)

request_embedding_examples = [
    RequestEmbedding(
        id=1,
        title="What are the most intelligent animals?",
        body="""
        <h1>Animal Intelligence</h1>

        <h2>Which animals are considered the smartest?</h2>
        <p>Some animals are known for their remarkable intelligence. Among them are dolphins, elephants, chimpanzees, and certain bird species like crows and parrots.</p>

        <h2>Key Traits of Intelligent Animals</h2>
        <ul>
            <li>Problem-solving abilities</li>
            <li>Use of tools</li>
            <li>Social behaviors</li>
            <li>Communication skills</li>
        </ul>
        """,
        categories=[general_questions_category],
    ),
    RequestEmbedding(
        id=2,
        title="Why do cats purr?",
        body="""
        <h1>Cats and Purring</h1>

        <h2>Understanding the Purr</h2>
        <p>Cats purr for several reasons: they may be happy, comfortable, or even in pain or distress. Purring is a form of communication and self-soothing.</p>

        <h2>Scientific Insight</h2>
        <p>Purring involves the rapid twitching of the laryngeal muscles, which controls the opening and closing of the space between the vocal cords.</p>
        """,
        categories=[general_questions_category],
    ),
    RequestEmbedding(
        id=3,
        title="How do migratory birds navigate?",
        body="""
        <h1>Migration Navigation</h1>

        <h2>Bird Migration</h2>
        <p>Birds migrate long distances to find better climates or breeding grounds. They navigate using the sun, stars, Earth's magnetic field, and landmarks.</p>

        <h2>Amazing Journeys</h2>
        <p>Some birds, like the Arctic Tern, travel thousands of kilometers between the poles annually.</p>
        """,
        categories=[general_questions_category],
    ),
    RequestEmbedding(
        id=4,
        title="What do dogs dream about?",
        body="""
        <h1>Dog Dreams</h1>

        <h2>Do Dogs Dream?</h2>
        <p>Yes, dogs dream just like humans. During REM sleep, dogs may relive their daily activities such as playing, chasing, or eating.</p>

        <h2>Observing Dreams</h2>
        <p>It's common to see dogs twitching, making sounds, or moving their paws while dreaming.</p>
        """,
        categories=[general_questions_category],
    ),
    RequestEmbedding(
        id=5,
        title="How do chameleons change color?",
        body="""
        <h1>Chameleon Color Change</h1>

        <h2>Mechanism Behind Color Change</h2>
        <p>Chameleons change color by manipulating specialized cells called chromatophores in their skin. These cells reflect light differently based on the arrangement of nanocrystals.</p>

        <h2>Why Do They Change Color?</h2>
        <ul>
            <li>Camouflage</li>
            <li>Temperature regulation</li>
            <li>Social signaling</li>
            <li>Stress responses</li>
        </ul>
        """,
        categories=[general_questions_category],
    ),
]
